from mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_scheme').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(fn)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_scheme').query_db(query, data)

    @classmethod
    def get_dojo_name(cls, dojo_id):
        query = 'SELECT name from dojos WHERE id = %(dojo_id)s;'
        data={'dojo_id':dojo_id}
        result =  connectToMySQL('dojos_and_ninjas_scheme').query_db(query, data)
        if len(result) == 0:
            return None
        return result[0]["name"]