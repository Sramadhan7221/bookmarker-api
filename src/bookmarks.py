from flask import Blueprint,request,jsonify
import validators
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_409_CONFLICT,HTTP_201_CREATED,HTTP_200_OK,HTTP_204_NO_CONTENT
from src.database import Bookmark,db
from flask_jwt_extended import get_jwt_identity,jwt_required
from flasgger import swag_from

bookmarks = Blueprint("bookmarks",__name__, url_prefix="/api/v1/bookmarks")

@bookmarks.route('/', methods=['POST','GET'])
@jwt_required()
def handle_bookmarks():
   current_user = get_jwt_identity()

   if request.method == 'POST':

      body = request.get_json().get('body', '')
      url = request.get_json().get('url', '')

      if not validators.url(url):
         return jsonify({
            'error': "Please Enter a valid Url "
         }),HTTP_400_BAD_REQUEST

      if Bookmark.query.filter_by(url=url).first():
         return jsonify({
            'error': "Bookmark is exist "
         }),HTTP_409_CONFLICT

      bookmark = Bookmark(url=url,body=body,user_id=current_user)   
      db.session.add(bookmark)
      db.session.commit()

      return jsonify({
         'id':bookmark.id,
         'url':bookmark.url,
         'short_url':bookmark.short_url,
         'visit':bookmark.visits,
         'created_at': bookmark.created_at,
         'updated_at': bookmark.updated_at
      }),HTTP_201_CREATED
   else:
      page = request.args.get('page',1, type=int)
      per_page = request.args.get('per_page',5, type=int)

      mybookmarks=Bookmark.query.filter_by(user_id=current_user).paginate(page=page, per_page=per_page)

      data = []

      for bookmark in mybookmarks.items:
         data.append({
            'id': bookmark.id,
            'url': bookmark.url,
            'short_url': bookmark.short_url,
            'visit': bookmark.visits,
            'body': bookmark.body,
            'created_at': bookmark.created_at,
            'updated_at': bookmark.updated_at
         })
      
      meta = {
         "page" : mybookmarks.page,
         "pages": mybookmarks.pages,
         "total_count": mybookmarks.total,
         "prev_page": mybookmarks.prev_num,
         "next_page": mybookmarks.next_num,
         "has_next": mybookmarks.has_next,
         "has_prev": mybookmarks.has_prev
      }
   return jsonify({
      'data':data,
      'meta':meta
   }),HTTP_200_OK

@bookmarks.get('/<int:id>')
@jwt_required()
def get_bookmark(id):
   curr_user = get_jwt_identity()

   bookmark = Bookmark.query.filter_by(user_id=curr_user, id=id).first()

   if not bookmark:
      return jsonify({'error': 'Item not found'}),HTTP_404_NOT_FOUND
   
   return jsonify({
      'id': bookmark.id,
      'url': bookmark.url,
      'short_url': bookmark.short_url,
      'visit': bookmark.visits,
      'body': bookmark.body,
      'created_at': bookmark.created_at,
      'updated_at': bookmark.updated_at
   }), HTTP_200_OK

@bookmarks.patch('/<int:id>')
@jwt_required()
def edit_bookmark(id):
   curr_user = get_jwt_identity()

   bookmark = Bookmark.query.filter_by(user_id=curr_user, id=id).first()

   if not bookmark:
      return jsonify({'error': 'Item not found'}),HTTP_404_NOT_FOUND
   
   body = request.get_json().get('body', '')
   url = request.get_json().get('url', '')

   if not validators.url(url):
      return jsonify({
         'error': "Please Enter a valid Url "
      }),HTTP_400_BAD_REQUEST

   bookmark.url = url
   bookmark.body = body

   db.session.commit()
   return jsonify({
         'id':bookmark.id,
         'url':bookmark.url,
         'short_url':bookmark.short_url,
         'visit':bookmark.visits,
         'created_at': bookmark.created_at,
         'updated_at': bookmark.updated_at
      }),HTTP_200_OK

@bookmarks.delete('/<int:id>')
@jwt_required()
def del_bookmark(id):
   curr_user = get_jwt_identity()

   bookmark = Bookmark.query.filter_by(user_id=curr_user, id=id).first()

   if not bookmark:
      return jsonify({'error': 'Item not found'}),HTTP_404_NOT_FOUND
   
   db.session.delete(bookmark)
   db.session.commit()

   return jsonify({}), HTTP_204_NO_CONTENT


@bookmarks.get("/stats")
@jwt_required()
@swag_from('./docs/bookmarks/stats.yaml')
def get_stats():
   curr_user = get_jwt_identity()
   data=[]

   items = Bookmark.query.filter_by(user_id=curr_user).all()

   for bookmark in items:
      new_link={
         'visits':bookmark.visits,
         'url': bookmark.url,
         'id': bookmark.id,
         'short_url': bookmark.short_url
      } 

      data.append(new_link)

   return jsonify({'data':data})