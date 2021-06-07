user_id=eval(document.getElementById('user_id').innerText)
console.log(user_id)
var config = {
    method: 'get',
    url: 'http://127.0.0.1:8000/plantas_registradas/',
    headers: { }
  };

axios(config)
.then(function (response) {
    var data=response.data;
    console.log(response.data)
    let your_data=[]
    for (let i=0; i<data.length; i++){
      if (eval(data[i].usuario)==user_id){
        your_data.push(data[i])

      }
    }
    data=your_data
    sessionStorage.setItem('all_data',JSON.stringify(data))
    let tabela=document.getElementById('plantas')
    for (let i=0; i<data.length; i++){

        let tb=`<tr>
        <td>${data[i].name}</td>
        <td>${data[i].species}</td>
        <td>${data[i].date}</td>
        <td><a href="/dados_planta" onclick='dadosPage("${data[i].name}","${data[i].species}")'>Ir</a></td>
        </tr>`

        tabela.innerHTML+=tb

      }

  })
  .catch(function (error) {
    console.log(error);
  });


function dadosPage( nome,especie)
{
    data={
        name:nome,
        species: especie
    };
    sessionStorage.setItem('data', JSON.stringify(data))
}


function apagarTudo(){
    
    if (!confirm('Tal ação não pode ser desfeita. Continuar mesmo assim?')){
        return
    }
    let data=JSON.parse(sessionStorage.getItem('all_data'))
    while (data.length>=0){
        deleted=data.pop()
        id=deleted.id
        var config = {
            method: 'delete',
            url: 'http://127.0.0.1:8000/plantas_registradas/'+id+'/',
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

}
  