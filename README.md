# Docker-Example

**How to use**

you can read complete explaintion on this <a href="https://medium.com/@vkmauryavk/practical-guide-to-docker-4f21ac979853" target="_blank">Blog Link </a>

Make a POST request to the /convert endpoint with a JSON object containing the input_str key and the string you want to convert as its value. The API will return a JSON object containing the output_list key and a list of the individual words in the input string.

Here's an example request:

<pre>
curl --location --request POST 'http://localhost:5000/convert' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_str": "Hello World"
}'

</pre>

And the corresponding response:

<pre>
{
    "output_list": [
        "Hello",
        "World"
    ]
}
</pre>

**Building and running the Docker image**

To build Docker 
<pre>
docker build -t myflaskapp .
</pre>

To run Docker
<pre>
docker run -p 5000:5000 myflaskapp

</pre>
