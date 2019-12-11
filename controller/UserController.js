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
                obj[item.name] = item.value;
            }
    
            userJson = JSON.stringify(obj);

            try{
                json = await conn.getUsersDB();
                
                //change to password
                
                console.log(json);

                

                for(let i = 0; i < json.length; i++){
                    if(obj.email == json[i].email && obj.password == json[i].name){
                        //Siguiente ventana
                        band = true;
                    }
                }

                console.log('Estado de acceso: ' + band);               
            }catch(err){
                console.log(err);
            }

            if(band){
                window.location.href = "dashboard.html";
            }

            console.log(userJson);
        }else{
            alert('Missed input field');
        }
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
        let pass2 = obj.confPassword;
  
        if(pass1 == pass2){
          band = true;
        }
        
        console.log(band);
        return band;
      }


}
