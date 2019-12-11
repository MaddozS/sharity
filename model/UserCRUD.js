function UserCRUD(){

    this.getUsersDB = async () => {
        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/users/');
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }

    this.postUsersDB = async (elemJson) => {

        console.log(elemJson);
        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/users/', {
                                    method: 'POST',
                                    body: elemJson,
                                    headers: {
                                    "Content-type": "application/json; charset=UTF-8"
                                    }
                                });

            const json = await response.json();

            console.log(json);

            console.log(response);
            
        }catch(e){
            console.log(e);
        }
    }

    this.updateUser = async (data) => {
        try{
            const response = await fetch('http://ec2-3-92-65-138.compute-1.amazonaws.com:5000/api/users/' + data.id, {
                                    method: 'PUT',
                                    body: data,
                                    headers: {
                                    "Content-type": "application/json; charset=UTF-8"
                                    }
                                });

            const json = await response.json();

            console.log(json);

            console.log(response);
            
        }catch(e){
            console.log(e);
        }
    }
}