document.addEventListener("DOMContentLoaded", ()=> {
var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect',()=>{

  document.querySelectorAll('button').forEach(button => {
    button.onclick = () => {
      const selection =button.dataset.vote;
      socket.emit('submit',{'selection':selection});
    };
  });
});

socket.on('my response', (data)=>{
  const li =document.createElement('li');
  li.innerHTML =`The response was ${data.selection}`;
  document.querySelector('#sarpong').append(li);

});


});
