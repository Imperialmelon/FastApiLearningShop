from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.backend.db_depends import get_db
from sqlalchemy import select, insert
from app.routers.auth import get_current_user
from app.schemas import CreateReview
from app.models.review import Review



router = APIRouter(prefix='/reviews', tags=['reviews'])

@router.get("/")
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    revs = await db.scalars(select(Review).where(Review.is_active==True))
    revs = revs.all()
    if not revs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no reviews'
        )
    return revs

@router.get("/{product_id}")
async def products_reviews(db: Annotated[AsyncSession, Depends(get_db)], product_id: int):
    reviews = await db.scalars(
        select(Review).where(Review.product_id==product_id)
    )
    return reviews.all()


@router.post("/add_review", status_code=status.HTTP_201_CREATED)
async def add_review(
    db: Annotated[AsyncSession, Depends(get_db)],
    create_review: CreateReview, 
    get_user: Annotated[dict, Depends(get_current_user)]
):
    user_id = get_user.get('id') 

    stmt = insert(Review).values(
        user_id=user_id,
        product_id=create_review.product_id,
        comment=create_review.comment,
        grade=create_review.grade,
    )
    await db.execute(stmt)
    await db.commit()

    return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }

@router.delete('/{review_id}')
async def delete_product(db: Annotated[AsyncSession, Depends(get_db)], review_id: int,
                         get_user: Annotated[dict, Depends(get_current_user)]):
    review_delete = await db.scalar(select(Review).where(Review.id == review_id))

    if review_delete is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no product found'
             )
    if get_user.get('is_admin'):
        review_delete.is_active = False
        await db.commit()
        return {
                'status_code': status.HTTP_200_OK,
                'transaction': 'Product delete is successful'
            }
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='You have not enough permission for this action'
            )
