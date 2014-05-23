/**
 * Perhaps more surprising for the Java programmer, functions are also objects in Scala.
 * It is therefore possible to pass functions as arguments, to store them in variables,
 * and to return them from other functions. This ability to manipulate functions as
 * values is one of the cornerstone of a very interesting programming paradigm called
 * functional programming.
 */
object Timer {
	def oncePerSecond(callback: () => Unit) {
		while (true) { callback(); Thread sleep 1000 }
	}
	
	def timeFlies() {
		println("time flies like an arrow...")
	}

	def main(args: Array[String]) {
		// oncePerSecond(timeFlies)
		
		// same as above, but with Anonymous Functions
		oncePerThreeSeconds(() => println("every three seconds we blink"))
	}
	
	def oncePerThreeSeconds(callback: () => Unit) {
		while (true) { callback(); Thread sleep 3000 }
	}
}
	
/** One important difference is that classes in Scala can have parameters */
class Complex(real: Double, imaginary: Double) {
	def re() = real
	def im() = imaginary
	
	// It should be noted that the return type of these two methods is not given explicitly.
	// It will be inferred automatically by the compiler
	// val c = Complex(1.5, 2.3)
}
