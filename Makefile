get-latest-js:
	curl https://htmxxx.fly.dev/script.min.js > static/htmxxx.js

deploy: get-latest-js
	fly deploy