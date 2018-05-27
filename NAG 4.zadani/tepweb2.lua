tempPin = 4
ledPin = 3
gpio.mode(ledPin, gpio.OUTPUT)
----------------------------------------------------TADY SE TVORI WEBOVY ROZHRANI-----------------------------------
srv=net.createServer(net.TCP, 1) 
srv:listen(80,function(conn) 
    conn:on("receive", function(client,request)
        local buf = "";
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then 
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP"); 
        end
        local _GET = {}
        if (vars ~= nil)then 
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do 
                _GET[k] = v 
		print("key "..k.." value "..v)
            end 
        end
------------------------------------------------------KONEC WEBOVYHO ROZHRANI---------------------------
	buf = buf.."<h1> Ahoj! Trablsutink!</h1>\n";
        buf = buf.."<p>Prejes si LEDku rozsvitit nebo zhasnout? <a href=\"?pin=BLIK!\"><button>BLIK!</button></a>";
        buf = buf.."<a href=\"?pin=CVAK!\"><button>CVAK!</button></a></p>\n";
	buf = buf.."<p>Zmer teplotu!<a href=\"?pin=TEPLOTA!\"><button>TEPLOTA!</button></a></p>\n";
-------	buf = buf.."<form src=\"/\">Prejes si LEDku zhasnout nebo rozsvitit? <select name=\"pin\" onchange=\"form.submit()\">\n";	
--	buf = buf.."<h2> Teplota venku je </h2>"..temperature.."\n";
        local _on,_off = "",""
------------------------------------------------------BLIK
        if(_GET.pin == "BLIK")then
              gpio.write(ledPin, gpio.HIGH);
------------------------------------------------------CVAK
        elseif(_GET.pin == "CVAK")then
              gpio.write(ledPin, gpio.LOW);
------------------------------------------------------TEPLOTA
	elseif(_GET.pin == "TEPLOTA")then
          temp = readTemp();
          buf = buf.."<h2> Teplota venku je </h2>"..temp.." *C";
	end
-----------------------------------------------------------
        client:send(buf);
        client:close();
        collectgarbage();
    end)
end)

function readTemp ()
  count = 0
  addr = ""
  temperature = 0
  ow.setup(tempPin)
  repeat
    count = count + 1
    addr = ow.reset_search(tempPin)
    addr = ow.search(tempPin)
    tmr.wdclr()
  until((addr ~= nil) or (count > 100))
  ow.reset(tempPin)
  ow.select(tempPin, addr)
  ow.write(tempPin, 0x44, 1)
  tmr.delay(1000000)
  present = ow.reset(tempPin)
  ow.select(tempPin, addr)
  ow.write(tempPin,0xBE,1)
  print("P="..present)
  data = nil
  data = string.char(ow.read(tempPin))
  for i = 1, 8 do
    data = data .. string.char(ow.read(tempPin))
  end
  print(data:byte(1,9))
  crc = ow.crc8(string.sub(data,1,8))
  print("CRC="..crc)
  if (crc == data:byte(9)) then
    t = (data:byte(1) + data:byte(2) * 256) * 625
    temperature = t / 10000
    t2 = t % 10000
  end
  tmr.wdclr()
  print(temperature)
  return temperature
end


