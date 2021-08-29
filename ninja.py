from mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"

        results = connectToMySQL('dojos_and_ninjas_scheme').query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_ninjas_from_dojo(cls, dojo_id):
        query = "SELECT ninjas.first_name, ninjas.last_name, ninjas.age, dojos.name FROM ninjas JOIN dojos ON ninjas.dojos_id = dojos.id AND ninjas.dojos_id = %(dojo_id)s;"
        data={'dojo_id':dojo_id}
        ninjas =connectToMySQL('dojos_and_ninjas_scheme').query_db(query,data)
        return ninjas

    @classmethod
    def save(cls, data):
        query= "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(fn)s, %(ln)s, %(age)s, NOW(), NOW(),%(dojo)s);"
        connectToMySQL('dojos_and_ninjas_scheme').query_db(query, data)