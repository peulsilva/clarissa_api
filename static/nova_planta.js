var today = new Date();

var date = today.getFullYear()

if (today.getMonth()+1<10)
  date+='-0'+(today.getMonth()+1)

else
  date+='-'+(today.getMonth()+1)

if (today.getDate()<10)
  date+='-0'+today.getDate()
else
  date+='-'+today.getDate()

document.getElementById('id_date').value=date

function gravarApi(){

  let photo = document.getElementById("image").files[0];
  let formData = new FormData();
  formData.append('name',document.getElementById('name').value)
  formData.append('species',document.getElementById('species').value)
  if (photo!=null)
    formData.append("image", photo);
  formData.append('date',document.getElementById('date').value)

  const headers = { 'Content-Type': 'multipart/form-data'};

  axios.post('http://127.0.0.1:8000/plantas_registradas/', formData, headers)
  .then(function (response) {
    console.log(JSON.stringify(response.data));
  })
  .catch(function (error) {
    alert(error)
  });

  };
  





