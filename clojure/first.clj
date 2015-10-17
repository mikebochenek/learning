;; from http://www.braveclojure.com/do-things/

(ns first.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))

(defn add
  "adding numbers"
  [x y]
  (+ x y))

(+ 1 2 3)

;; (javax.swing.JOptionPane/showMessageDialog nil "Hello World")

(str "It was the panda " "in the library " "with a dust buster")

;; if else
(if true
  "abra cadabra"
  "hocus pocus")

(if true
  (do (println "Success!")
      "abra cadabra")
  (do (println "Failure :(")
      "hocus pocus"))

(nil? 1)
(nil? nil)

;; testing for equality
(= 1 1)

;; maps
(get {:a 0 :b 1} :b)

(get {:a 0 :b {:c "ho hum"}} :b)

(get {:a 0 :b 1} :c "UNICORNS")

;; vectors
(get [3 2 1] 0)

(hash-set 1 1 3 1 2)

(sorted-set :b :a :c)

(def failed-movie-titles ["Gone With the Moving Air" "Swellfellas"])

;; Identity returns its argument
(identity 'test)

;; and an example of quoting
'failed-movie-titles

(eval 'failed-movie-titles)

;;It is better to have 100 functions operate on one data structure
;;than 10 functions on 10 data structures.  -- Alan Perlis


;; functions
;; Return value of "or" is first truthy value, and + is truthy
(or + -)

((or + -) 1 2 3)


;; Return value of "and" is first falsey value or last truthy value.
;; + is the last truthy value
((and (= 1 1) +) 1 2 3)


;; The "inc" function increments a number by 1
(inc 1.1)

(map inc [0 1 2 3])

;; Here's the function call. It kicks off the evaluation process
(+ (inc 199) (/ 100 (- 7 2)))

;;  Anonymous Functions Example
(map (fn [name] (str "Hi, " name))
     ["Darth Vader" "Mr. Magoo"])

;; Another example
((fn [x] (* x 3)) 8)

;; compact form
(#(* % 3) 8)

;; if your anonymous function takes multiple arguments, you can distinguish them like this: %1, %2, %3, etc. % is equivalent to %1:


;; Returning Functions: Functions can return other functions. The returned functions are closures, which means that 
;; they can access all the variables that were in scope when the function was created.

;; inc-by is in scope, so the returned function has access to it even
;; when the returned function is used outside inc-maker
(defn inc-maker
  "Create a custom incrementor"
  [inc-by]
  #(+ % inc-by))

(def inc3 (inc-maker 3))

(inc3 7)



(.toUpperCase "By Bluebeard's bananas!")

(java.lang.Math/abs -3)