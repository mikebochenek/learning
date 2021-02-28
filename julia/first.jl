println(30+40)

# Unlike named functions, g is simply a function in a variable and can be overwritten at any time: 
g = (x,y) -> 2x+y
println(g(3,2))

println(rand(3))

# even though factorial is a built in faction, we try to create one i.e. https://rosettacode.org/wiki/Factorial#Julia
function fact(n::Int64)
    n < 0 && return zero(n)
    f = one(n)
    for i in 2:n
        f *= i
    end
    return f
end
 
for i in 10:20
	println("$i -> ", fact(Int64(i)))
end


# http://www.pkofod.com/2017/04/24/timing-in-Julia/
function speedtest(n)
    A = rand(n, n)
    b = rand(n)
    @time A\b
end

speedtest(1)
