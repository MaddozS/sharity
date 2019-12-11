function UserController(){
    
    let obj = {};
    let userJson;

    this.setUserJson = async (reg) => {

        let conn = new UserCRUD();
        let json;
        let band = false;

        if(this.validateForm(reg)){
            for(let i = 0 ; i < reg.length - 1; i++){
                let item = reg.item(i);
                obj[item.type] = item.value;
            }
    
            userJson = JSON.stringify(obj);

            try{
                json = await conn.getUsersDB();
                
                    //change to password
                for(let i = 0; i < json.length; i++){
                    if(obj.email == json[i].email && obj.password == json[i].name){
                        //Siguiente ventana
                        band = true;
                    }
                }           
            }catch(err){
                console.log(err);
            }

            if(band){
                window.location.href = "dashboard.html";
            }
        }else{
            alert('Missed input field');
        }
    }

    this.registerUser = async () => {
        let conn = new UserCRUD();

        conn.postUsersDB(userJson);
    }

    this.validateForm = (val) => {
        let band = true;

        for(let i = 0 ; i < val.length - 1; i++){
            let item = val.item(i);
            if(item.value == ''){
                band = false;
            }
        }

        return band;
    }

    this.passConf = () => {
        let band = false;
  
        let pass1 = obj.password;
        let pass2 = document.getElementById('exampleInputPassword1').value;
  
        if(pass1 == pass2){
          band = true;
        }
        
        console.log(band);
        return band;
      }


}
