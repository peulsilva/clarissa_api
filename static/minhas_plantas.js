


function dadosPage( nome)
{
    document.cookie='data='+nome
    sessionStorage.setItem('data', JSON.stringify(nome))
}


