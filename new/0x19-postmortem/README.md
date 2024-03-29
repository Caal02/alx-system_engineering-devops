#  		Postmortem
Postmortem for Alx Project Below is a postmortem for a webstack debugging assignment for Alx School. A simple website utilizing was returning a 500 status code to any GET requests. Students were tasked with identifying the problem and creating a Puppet script for the solution.

## Summary:  
Apache server was returning a 500 error for all GET requests. The website consists of one HTML page so problem with MySQL or PHP was identified as the likely culprit.The issue is started at 29–02–2023, 12:03 AM PDT causing error every timewhile trying to acces the server up to 9–02–2023, 12:06 AM PDT

## Timeline:
29–02–2023, 12:00 AM PDT: Project release 29–02–2023, 1:00 PM PDT: Begin project. First check for error logs. 29–02–2023, 1:20 PM PDT: Find that error logging for PHP was disabled. Error logging re-enabled, server restarted, ‘no such file’ error found. 29–02–2023, 1:45 PM PDT: Typographical error found in PHP file. Manually fix. Server restarted. Request returns 200 status code. 29–02–2023, 2:30 PM PDT: Puppet script begun and testing for proper fix begin 29–02–2023, 4:00 PM PDT: Puppet script finished and able to be deployed across all servers. Script pushed to GitHub

## Impact: 
Users unable to access website from at least midnight 29–02–2023 to 4:00 PM 29–02–2023. All servers affected by outage.

## Root Cause: 
Root cause of problem was a typogrpahical error for file name at line 137 of the file /var/www/html/wp-settings.php. Line read: require_once( ABSPATH . WPINC . ‘/class-wp-locale.phpp’ ); Extension for file should have been ‘.php’ Error likely caused by human error in updated settings and subsequent lack of testing to ensure server was still functional.

## Solution: 
Upon finding of error, a manual fix on one server was first completed to ensure the fix would work. A puppet file was then created to distribute across all servers.

## Prevention:  
Error could have been easily prevented from user who updated config file to test that the server was still functional before exiting. In addition, debugging should not have been turned off for PHP files. The fix was quite obvious when error logging was turned back on. Testing procedures must be more strcitly enforced for production environments in future situations as well as more stringent monitoring and protection of who has access to write to config files.

The link for the full blog => 
[@medium](https://medium.com/@caaleb02/postmortem-webstack-debugging-4bead8041cc3)
