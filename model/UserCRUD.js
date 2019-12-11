function UserCRUD(){

    this.getUsersDB = async () => {
        try{
            const response = await fetch('https://jsonplaceholder.typicode.com/comments?postId=1');
            const json = await response.json();

            return json;
                
        }catch(error){
            console.log(error);
        }
    }
}