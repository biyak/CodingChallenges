defmodule Fib do
  @moduledoc """
  Documentation for Fib.
  Author: Biya Kazmi
  Student ID: 400018251
  Course: Distributed Computing 4X03
  """

  def fib_calc(0) do 0 end

  def fib_calc(1) do 1 end

  def fib_calc(2) do 1 end

  def fib_calc(n) do
    fib_calc(n-1) + fib_calc(n-2)
  end 

  def server(caller) do
    send(caller,{ :ready, self()})
    receive do
      {:compute, n, client} -> 
          result = fib_calc(n)
          #IO.inspect([:answer, n, result])
      		send(client, {:answer, n, result})
      		server(caller)

          #client <- { :answer, n, fib_calc(n)}
      { :shutdown } -> exit(0)

    end

  end

end

# Fib.spawnServer()
 

# start_pid = self()
# pid = spawn(fn ->Fib.server(start_pid) end)
# send(pid, {:compute,6, start_pid})


defmodule Scheduler do
  def start(num_servers, job_list) do
    n = num_servers
    if n>0 do
      spawnServer()
      n = n - 1
    end

    run(num_servers, job_list, [])
  end

  def spawnServer() do
     spawn(Fib, :server, [self()])
  end

  def run(0, job_list, result_list) do
    #IO.inspect result_list
    result_list
  end

  def run(num_servers, job_list, result_list) do

    receive do #listens for messages from the server instances
      # gets a hi im ready repsonse from one of the processes
      {:ready, server_pid} -> 
        #checks if job list is non empty
        if length(job_list) == 0 do
          #If it is empty then tell this p to shutdown
          #and run again so that all other p can shut down
          send(server_pid, {:shutdown}) 
          run(num_servers-1,job_list,result_list)

        else
          #seperate into the job that needs doing next and 
          # rest of the jobs. 
          [head | tail] = job_list
          send(server_pid, {:compute, head, self()})

          job_list = tail

          run(num_servers, job_list, result_list)
        end

      #once you recieve a result from a process, put into result list 
      {:answer, n, result} -> result_list = result_list ++ [result]
            run(num_servers, job_list, result_list)

    end

  end

end

Scheduler.start(1, [1,2,3,4,5,6])

defmodule FibFast do

  def fib_calc(0) do 0 end

  def fib_calc(1) do 1 end

  def fib_calc(2) do 1 end

  def fib_calc(n) do
    cache = List.duplicate(0,n-1)
    cache = List.insert_at(cache, 1, 1)
    cache = List.insert_at(cache, 2, 1)

    #IO.inspect cache

    helper(cache, n)

  end 

  def helper(cache, n) do

    if n < 1 do
      0
    end

    if n <= 2 do
      1
    end

    #IO.puts Enum.at(cache, n)

    if (Enum.at(cache, n)) != 0 do
      value = Enum.at(cache, n)
      #IO.inspect cache
      cache = List.insert_at(cache, n, value)
      cache = List.delete_at(cache, n+1)
      value
    else 
      value = helper(cache, n-1) + helper(cache, n-2)
      # put the value into cache(n)
      cache = List.insert_at(cache, n, value)
      cache = List.delete_at(cache, n+1)
      #IO.inspect cache
      #IO.puts value
      value #and return that value 
    end
  end

end

value = FibFast.fib_calc(8)
IO.puts value


