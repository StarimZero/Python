from dao import db


def list(args):
    page = int(args.get('page'))
    size = int(args.get('size'))
    start = (page-1) * size
    try:
         with db.connection.cursor() as cursor:
             sql = "select *, date_format(bbs_regDate, '%%Y년-%%m월-%%d일 %%T') fmtdate from bbs order by bbs_id desc limit %s, %s"
             cursor.execute(sql, (start, size))
             return cursor.fetchall()
    except Exception as err :
        print('목록출력 에러 : ', err)
    finally:
        cursor.close()

def total():
    try:
        with db.connection.cursor() as cursor:
            sql = "select count(*) cnt from bbs"
            cursor.execute(sql)
            return cursor.fetchone()
    except Exception as err :
        print("토탈구하다가 에러 : ", err)
    finally:
        cursor.close()

def insert(bbs):
    try:
         with db.connection.cursor() as cursor:
             sql = " insert into bbs(bbs_writer, bbs_title, bbs_contents) values (%s, %s, %s)"
             cursor.execute(sql, (bbs.get('writer'), bbs.get('title'), bbs.get('contents')))
             db.connection.commit()
             return "success"
    except Exception as err:
        print("게시물등록오류 : ", err)
        return "fail"
    finally :
        cursor.close();

def delete(bid):
    try:
        with db.connection.cursor() as cursor:
            sql = " delete from bbs where bbs_id=%s"
            cursor.execute(sql, bid)
            db.connection.commit()
            return "success"
    except Exception as err:
        print("게시물삭제오류 : ", err)
        return "fail"
    finally :
        cursor.close();

def read(bid):
    try:
        with db.connection.cursor() as cursor:
            sql = "select * from bbs where bbs_id=%s"
            cursor.execute(sql, bid)
            row = cursor.fetchone()
            return row
    except Exception as err:
        print("게시물읽기오류 : ", err)
        return "fail"
    finally :
        cursor.close();

def update(bbs):
    try:
         with db.connection.cursor() as cursor:
             sql = " update bbs set bbs_title=%s, bbs_contents=%s where bbs_id=%s"
             cursor.execute(sql, (bbs.get('bbs_title'), bbs.get('bbs_contents'), bbs.get('bbs_id')))
             db.connection.commit()
             return "success"
    except Exception as err:
        print("게시물 수정오류 : ", err)
        return "fail"
    finally :
        cursor.close();
