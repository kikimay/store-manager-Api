users = [
    {
        "admin":True,
        "email":"mwirigi@gmail.com",
        "name":"maryn",
        "password":"pass",
        "user_id":1,
        "username":"kiki"
    }
]

class Users(object):
    @app.route("/api/v1/register", methods=["POST"])
    def register():#define a method that registers a user
        if not request.is_json:
            return make_response(jsonify({"status":"wrong format","messenge":"request not json"}),400)
        else:
            data = request.get_json() 
            user_id =  len(users)+1
            name = data['name']
            email = data['email']
            username = data['username']
            password = data['password']
            password2 = data['password2']

        
        if not password == password2:#check if the two passwords match
            return make_response(jsonify({"status":"not acceptable","messenge":"passwords don't match"}),406)

        if name == "" or email == "" or username == "" or password == "" or password2 == "":
            return make_response(jsonify({"status":"not acceptable","messenge":"Please fill all the required fields"}),406)#check if name,email,username,password,password2 are empty
       
        if not re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email, re.IGNORECASE):
            return make_response(jsonify({"status":"not acceptable","messenge":"Email Provided is not in email format"}),406)#check email format
       
        
        if len(users) > 0:
            for user in users:
                e = user.get('email')#gets all the email adresses for all the existing users.
                
                if email == e:
                    return make_response(jsonify({"status":"not acceptable","messenge":"user already exists"}),406)#check if email adress provided matches one that already exists
                
                else:
                    user = {
                        "user_id":user_id,
                        "name":name,
                        "email":email,   
                        "username":username,
                        "password":password,
                        "admin":False
                        }

                     
                    
                   
        else:
            user = {
                 "user_id":user_id,
                 "name":name,
                 "email":email,   
                 "username":username,
                 "password":password,
                 "admin":False
                 }

        users.append(user)#add user to the list of users if the email provided doesnt match one of the existing users

        return make_response(jsonify({"status":"created", "user":user, "users":users }),201)


