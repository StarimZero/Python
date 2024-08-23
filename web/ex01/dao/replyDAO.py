from dao import db

def list(bid, args):
    page = int(args['page'])
    size = int(args['size'])
    start = (page-1)*size
    try:
         with db.connection.cursor() as cursor:
            sql = "select *, date_format(reply_regDate, '%%Y년-%%m월-%%d일 %%T') fmtdate \
                from reply where bbs_id=%s order by reply_id desc limit %s, %s"
            cursor.execute(sql, (bid, start, size))
            rows = cursor.fetchall()
            return rows
    except Exception as err :
        print("댓글목록오류 : ", err)
    finally:
        cursor.close();

def insert(reply):
    try:
        with db.connection.cursor() as cursor:
            sql = "insert into reply (bbs_id, reply_contents, reply_writer)  values(%s, %s, %s)"
            cursor.execute(sql, (reply.get('bid'), reply.get('contents'), reply.get('uid')))
            db.connection.commit()
            return 'success'
    except Exception as err :
        print("댓글쓰다가 오류 : ", err)
        return 'fail'
    finally:
        cursor.close();

def total(bid):
  try:
    with db.connection.cursor() as cursor:
      sql="select count(*) cnt from reply where bbs_id=%s"
      cursor.execute(sql, bid)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print("댓글 total구하다가 오류 : ", err)
  finally:
    cursor.close();


def delete(rid):
    try:
        with db.connection.cursor() as cursor:
            sql = "delete from reply where reply_id=%s"
            cursor.execute(sql, rid)
            db.connection.commit()
            return 'success'
    except Exception as err :
        print("댓글삭제하다가 오류 : ", err)
        return 'fail'
    finally:
        cursor.close();

def update(reply):
    try:
        with db.connection.cursor() as cursor:
            sql = "update reply set reply_contents=%s, reply_regDate=now() where reply_id=%s"
            cursor.execute(sql, (reply.get('contents'), reply.get('rid')))
            db.connection.commit()
            return 'success'
    except Exception as err :
        print("댓글수정하다가 오류 : ", err)
        return 'fail'
    finally:
        cursor.close();
