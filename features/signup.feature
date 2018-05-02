@tags @tag
Feature: Read data from socket 
  description
  Connect to port and read data from socket
  
  
Scenario: Run Dump on default PC and default port 
   Given Server is running on port 4444
    When dumper is started with lol.txt
	Then we can kill server
    Then Output is empty
    Then Error is empty
    Then Exit code is 0
    Then Expected file is created and same with lol1.txt
		


   
Scenario: Run Dump on default PC and not default port (server runs on other port) 
   Given Server is running on port 4444
    When dumper is started: lol3.txt and 8888
	Then we can kill server
    Then Refused Error appears 
	
Scenario: Server is not started run dumper
    When dumper is started with lol4.txt
    Then Refused Error appears 

Scenario: Run Dump with 3 arguments 
   Given Server is running on port 4444
    When Dump  with 3 arguments started: lol3.txt and 4444 and localhost
	Then we can kill server
    Then Output is empty
    Then Error is empty
    Then Exit code is 0
    Then Expected file is created and same with lol1.txt
	



   


	  
	  
	  
          
  

 

