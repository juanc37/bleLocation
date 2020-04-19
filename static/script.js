//currently dispalys name , but will need to be changed

//unction init(){
  //document.getElementById('submit').addEventListener('click',addDoctor);
//}

function addDoctor(){
  document.getElementById('displayName').innerHTML = 
            document.getElementById("doctor_id").value;
}

//document.addEventListener('DOMContentedLoaded',init);