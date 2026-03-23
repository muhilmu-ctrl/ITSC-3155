from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, db_recipe):
    return db.query(models.Recipe).filter(models.Recipe.id == db_recipe).first()

def update(db: Session, db_recipe: int, recipe: schemas.RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == db_recipe)
    update_data = recipe.model_dump(exclude_unset=True)
    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()

def delete(db: Session, db_recipe: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == db_recipe)
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)