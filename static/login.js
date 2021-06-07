class Data{
    constructor(username){
        this.username=username
    }
    
}

class DB{
    constructor(){
        if (localStorage.getItem('id')===null)
            localStorage.setItem('id', '0')
    }

    getId(){
        let id=localStorage.getItem('id')
        id=eval(id)+1
        id=id.toString()
        localStorage.setItem('id',id)
        return id
    }
    gravar(data){
        let id=this.getId()
        localStorage.setItem(id,JSON.stringify(data))
        
    }
    
    
}

function saveUser(){
    localStorage.clear()
    db=new DB()
    user=new Data(document.getElementsByName('username')[0].value)
    db.gravar(user)
}