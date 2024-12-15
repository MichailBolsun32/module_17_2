from fastapi import APIRouter

#В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user',
router = APIRouter(prefix='/user', tags=["user"])

# а также следующие маршруты, с пустыми функциями:
    # get '/' с функцией all_users.
@router.get("/")
async def all_tasks():
    pass

# get '/user_id' с функцией user_by_id.
@router.get("/task_id")
async def user_by_id():
    pass

# post '/create' с функцией create_user.
@router.post('/create')
async def create_user():
    pass

# put '/update' с функцией update_user.
@router.put("/update")
async def update_user():
    pass

# delete '/delete' с функцией delete_user.
@router.delete("/delete")
async def delete_user():
    pass