let data=JSON.parse(sessionStorage.getItem('data'))
document.cookie='data='+data

function reload(){
  if (localStorage.getItem('reloaded')==undefined){
    window.location = '/dados_planta'
    localStorage.setItem('reloaded', '1')
  }
  else{
    localStorage.removeItem('reloaded')
  }
    
}

