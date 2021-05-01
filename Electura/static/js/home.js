function complete(id, name, description, ele){
	let http_request = new XMLHttpRequest();
	completed_ele = document.getElementsByClassName('completed')[0];
	var individual = document.createElement('div');
	individual.classList.add('individual_task');
	var task_name = document.createElement('h3');
	task_name.innerHTML = name + "<span class='pending_tag'>completed</span>";
	var task_description = document.createElement('p');
	task_description.innerHTML = description;
	individual.appendChild(task_name);
	individual.appendChild(task_description);
	completed_ele.appendChild(individual);
	ele.parentElement.remove();

	http_request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
		}
	}
	http_request.open("GET", "completed/" + id, true);
	http_request.send();
}

var ul = document.getElementsByTagName('ul')[0];

function display(){
	ul.style.opacity = '1';
	ul.style.transform = 'translateY(0px)';
	ul.style.pointerEvents = 'all';
}

var notifications = document.getElementById('notifications');
var very = document.getElementById('very_special');
var counter = 0;
notifications.addEventListener('click', () =>{
	if(counter == 0){
		very.innerHTML = "Notifications <i class='fas fa-caret-up'></i>";
		ul.style.opacity = '1';
		ul.style.transform = 'translateY(0px)';
		ul.style.pointerEvents = 'all';
		counter = 1;
	}
	else{
		very.innerHTML = "Notifications <i class='fas fa-caret-down'></i>";
		ul.style.opacity = '0';
		ul.style.transform = 'translateY(-10px)';
		ul.style.pointerEvents = 'none';
		counter = 0;
	}

});


function read(ele, id){
	let http_request = new XMLHttpRequest();
	http_request.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
		}
	}
	http_request.open("GET", "read/" + id, true);
	http_request.send();
	ele.parentElement.remove();
	if(ul.children.length == 0){
		document.getElementById("new_icon").remove();
		ul.innerHTML = "<li>There are no new notifications</li>";
	}
}