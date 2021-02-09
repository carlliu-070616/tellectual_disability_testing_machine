import click
import os


from main import app,db
from main.models import User


@app.cli.command()
@click.option('--drop', is_flag=True, help='删除后创建')
def initdb(drop):
   if drop:
      click.confirm('你想删除全部数据吗？', abort=True)
      db.drop_all()
      click.echo('已删除')
   db.create_all()
   admin = User.query.filter_by(is_admin=True).first()
   if admin:
      password = os.getenv("ADMIN_PASSWORD")
      username = os.getenv("ADMIN_USERNAME")
      admin.username = username
      admin.set_password(password)
   else:
      password = os.getenv("ADMIN_PASSWORD")
      username = os.getenv("ADMIN_USERNAME")
      name = os.getenv("ADMIN_NAME")
      email = os.getenv("ADMIN_EMAIL")
      admin = User(username=username,name=name,email=email,Intellectual_disability=0,is_admin=True)
      admin.set_password(password)
      db.session.add(admin)
   db.session.commit()
   click.echo('已完成')