let nome= document.getElementById('nome')
let especie=document.getElementById('especie')
let idade=document.getElementById('idade')
let img=document.getElementById('img')

let data=JSON.parse(sessionStorage.getItem('data'))

function find (arr, name){
    for (let i=0; i<arr.length; i++){
        if (arr[i].name==name){
            return i
        }
    }
}

var config = {
    method: 'get',
    url: 'http://127.0.0.1:8000/plantas_registradas/',
    headers: { }
  };
  
  axios(config)
  .then(function (response) {
    i= find(response.data,data.name)
    data=response.data[i]
    nome.innerHTML=data.name
    especie.innerHTML= 'Espécie: '+ data.species

    date=new Date(data.date)

    decorrido=Date.now()-date
    decorrido=Math.floor(decorrido/(1000*3600*24))

    idade.innerHTML= decorrido + ' dias'

    img.src=data.image
  })
  .catch(function (error) {
    console.log(error);
  });

function Delete(){
        var config = {
        method: 'delete',
        url: 'http://127.0.0.1:8000/plantas_registradas/'+data.id+'/',
        headers: { }
      };
      
      axios(config)
      .then(function (response) {
        return
      })
      .catch(function (error) {
        console.log(error);
      });
      
}
  