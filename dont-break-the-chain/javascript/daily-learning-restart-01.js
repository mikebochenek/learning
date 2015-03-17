/* My First Closure
 * In its most basic form, a closure is simply an outer function that returns 
 * an inner function. Doing this creates a mechanism to return an enclosed scope
 * on demand. Here is a simple closure: */

function outer(name) {
  var hello = "hi", inner;   
  return inner = function() {    
    return hello + " " + name;  
  };
} 
// Create and use the closurevar 
name = outer("mark")(); 

// => 'hi mark'
console.log(name);

/* As you learned in the previous chapter, JavaScript introduced a new function style: 
 * the so-called fat arrow. Let’s rewrite the previous example using the fat arrow: */

var outer (name) => {  
  var hello = "hi", inner;   
  inner => hello + " " + name;
}
var name = outer("mark")(); 
// => 'hi mark'
console.log(name);

/* In these two examples, you can see that the local variable hello can be 
 * used in the return statement of the inner function. At the point of execution,
 * hello is a free variable belonging to the enclosing scope. 
 * This example borders on meaninglessness, though, so let’s look at a 
 * slightly more complex closure: */

var car;
function carFactory(kind) {  
  var wheelCount, start;  
  wheelCount = 4;  
  start = function() {    
    console.log('started with ' + wheelCount + ' wheels.');  
  
    // Closure created here.  
    return (function() {    
      return {
        make: kind, 
	    wheels: wheelCount,      
	    startEngine: start
	  };
    }();
  }    
  
  car = carFactory('Tesla'); 
};   

// => Tesla
console.log(car.make); 

// => started with 4 wheels.
car.startEngine();

