## Dependencies

These distributions will be installed automatically when installing Flask.
<ul>
<li>
<strong style="color:rgba(86, 224, 178, 1)">Werkzeug</strong> implements WSGI, the standard Python interface between applications and servers.
</li>
<li>
<strong style="color:rgba(86, 224, 178, 1)">Jinja</strong> is a template language that renders the pages your application serves.
</li>
<li>
<strong style="color:rgba(86, 224, 178, 1)">MarkupSafe</strong> comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
</li>
<li>
<strong style="color:rgba(86, 224, 178, 1)">ItsDangerous</strong> securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
</li>
<li>
<strong style="color:rgba(86, 224, 178, 1)">Click</strong> is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
</li>
<li>
<strong style="color:rgba(86, 224, 178, 1)">Blinker</strong> provides support for Signals.
</li>
</ul>



# Cookies

```plain
      -o, --output <file>
            Write output  to the  given file  instead of  stdout.  If you  are
            using globbing to fetch multiple  documents, you should quote  the
            URL and you  can use  "#" followed  by a number  in the  filename.
            That variable is  then replaced  with the current  string for  the
            URL being fetched. Like in:

                curl "http://{one,two}.example.com" -o "file_#1.txt"

            or use several variables like:

                curl "http://{site,host}.host[1-5].example" -o "#1_#2"

            You may use this  option as many times as  the number of URLs  you
            have. For example,  if you specify  two URLs  on the same  command
            line, you can use it like this:

                curl -o aa example.com -o bb example.net

            and the order  of the  -o options  and the URLs  does not  matter,
            just that the  first -o is  for the first  URL and  so on, so  the
            above command line can also be written as

                curl example.com example.net -o aa -o bb

            See also the --create-dirs option to create the local  directories
            dynamically. Specifying the output as  '-' (a single dash)  passes
            the output to stdout.

            To  suppress  response   bodies,  you  can   redirect  output   to
            /dev/null:

                curl example.com -o /dev/null

            Or for Windows:

                curl example.com -o nul

            Specify the  filename  as single  minus  to force  the  output  to
            stdout, to  override curl's  internal  binary output  in  terminal
            prevention:

                curl https://example.com/jpeg -o -
            --output can be used several times in a command line

            Examples:
             curl -o file https://example.com
             curl "http://{one,two}.example.com" -o "file_#1.txt"
             curl "http://{site,host}.host[1-5].example" -o "#1_#2"
             curl -o file https://example.com -o file2 https://example.net

            See      also      --remote-name,      --remote-name-all       and
            --remote-header-name.



   -b, --cookie <data|filename>
            (HTTP) Pass the data to the  HTTP server in the Cookie header.  It
            is supposedly the data  previously received from  the server in  a
            "Set-Cookie:"  line.   The   data   should  be   in   the   format
            "NAME1=VALUE1; NAME2=VALUE2" or as a single filename.

            When given a set of specific cookies and not a filename,  it makes
            curl use the  cookie header  with this content  explicitly in  all
            outgoing  request(s).  If  multiple  requests  are  done  due   to
            authentication, followed redirects or  similar, they all get  this
            cookie header passed on.

            If no "=" symbol  is used in the  argument, it is instead  treated
            as a filename to read  previously stored cookie from. This  option
            also activates the cookie engine which makes curl record  incoming
            cookies, which may be handy  if you are using this in  combination
            with the --location  option or  do multiple URL  transfers on  the
            same invoke.

            If the filename is a  single minus ("-"), curl reads the  contents
            from stdin. If  the filename is  an empty string  ("") and is  the
            only cookie input,  curl activates the  cookie engine without  any
            cookies.

            The file format of the file  to read cookies from should be  plain
            HTTP headers  (Set-Cookie style)  or the  Netscape/Mozilla  cookie
            file format.

            The file  specified  with  --cookie  is only  used  as  input.  No
            cookies are  written  to that  file.  To store  cookies,  use  the
            --cookie-jar option.

            If you use the Set-Cookie file format and do not specify  a domain
            then the cookie  is not sent  since the  domain never matches.  To
            address  this,  set  a  domain  in  Set-Cookie  line  (doing  that
            includes subdomains) or preferably: use the Netscape format.

            Users often  want  to both  read cookies  from  a file  and  write
            updated cookies  back  to  a  file, so  using  both  --cookie  and
            --cookie-jar in the same command line is common.

            If curl  is  built  with  PSL (Public  Suffix  List)  support,  it
            detects and discards  cookies that are  specified for such  suffix
            domains that should  not be allowed  to have  cookies. If curl  is
            not built  with  PSL support,  it has  no  ability to  stop  super
            cookies.

            --cookie can be used several times in a command line

            Examples:
             curl -b "" https://example.com
             curl -b cookiefile https://example.com
             curl -b cookiefile -c cookiefile https://example.com
             curl -b name=Jane https://example.com

            See also --cookie-jar and --junk-session-cookies.
```

```plain

-j, --junk-session-cookies
            (HTTP) When curl is told to  read cookies from a given file,  this
            option makes it discard all  "session cookies". This has the  same
            effect as if a  new session is  started. Typical browsers  discard
            session cookies when they are closed down.

            Providing  --junk-session-cookies  multiple  times  has  no  extra
            effect. Disable it again with --no-junk-session-cookies.

            Example:
             curl --junk-session-cookies -b cookies.txt https://example.com

            See also --cookie and --cookie-jar.

```