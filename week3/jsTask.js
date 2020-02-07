function add(){
       if(document.getElementById("usr").value != ""){
            var li = document.createElement("li");
            var button = document.createElement("button");
            button.type = "button";
            button.className = "cancel";
            button.innerHTML = "X";
            button.onclick = function(){
                document.getElementById("list").removeChild(li);
            }
            li.appendChild(document.createTextNode(document.getElementById("usr").value));
            li.appendChild(button);
            document.getElementById("list").appendChild(li);
            document.getElementById("usr").value = "";
        }
        else alert("Input is empty!");
}