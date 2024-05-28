function display_currtime() {
    let curr_time = new Date()
    alert("The current time is:" + curr_time);
}

display_currtime(); //display immediately for the first time 
setInterval(display_currtime, 10000); //every 10 secs   