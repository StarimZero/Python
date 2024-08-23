from dao import db

def list(page, size):
  page = int(page)
  size = int(size)
  start = (page - 1) * size
  try:
    with db.connection.cursor() as cursor:
      sql = "select *, date_format(bbs_regDate, '%%Y년-%%m월-%%d일 %%T') fmtdate \
             from bbs order by bbs_id desc\
             limit %s, %s"
      cursor.execute(sql, (start, size))
      rows = cursor.fetchall()
      return rows
  except Exception as err:
    print('목록오류:', err)
  finally:
    cursor.close()


def insert(bbs):
    try:
      with db.connection.cursor() as cursor:
        sql = "insert into bbs (bbs_title, bbs_contents, bbs_writer) \
                values(%s, %s, %s)"
        cursor.execute(sql, (bbs.get('title'), bbs.get('contents'), bbs.get('uid')))
        db.connection.commit()
        return 'success'
    except Exception as err:
      print('글쓰기오류 : ', err)
      return 'fail'
    finally:
      cursor.close()
  

def read(bbs_id):
  try:
    with db.connection.cursor() as cursor:
      sql="select *, date_format(bbs_regDate, '%%Y-%%m-%%d %%T') fmtdate from bbs where bbs_id = '%s' order by bbs_id desc "
      cursor.execute(sql, bbs_id)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print("읽기오류: ", err)
  finally:
    cursor.close();
  

def delete(bid):
    try:
        with db.connection.cursor() as cursor:
            sql ="delete from bbs where bbs_id='%s'"
            cursor.execute(sql, bid)
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('글삭제오류 : ', err)
        return 'fail'
    finally:
        cursor.close()

def update(bbs):
    try:
      with db.connection.cursor() as cursor:
        sql = "update bbs set bbs_title=%s, bbs_contents=%s, bbs_regDate=now() where bbs_id=%s" 
        cursor.execute(sql, (bbs.get('title'), bbs.get('contents'), bbs.get('bid')))
        db.connection.commit()
        return 'success'
    except Exception as err:
      print('글수정 오류 : ', err)
      return 'fail'
    finally:
      cursor.close()

def total():
  try:
    with db.connection.cursor() as cursor:
      sql="select count(*) cnt from bbs"
      cursor.execute(sql)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print("total구하다가 오류 : ", err)
  finally:
    cursor.close();













