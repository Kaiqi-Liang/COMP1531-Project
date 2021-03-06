#!/bin/sh
# curl parameters
# -s --silent: Don't show progress meter or error messages, but still output the data or even stdout
# -S --show-error: When use with -s it makes curl show an error message if it fails
# -X --request <command>: CRUD or default GET when not specified
# -d --data <data>: json: -d '{"key1":"value1","key2":"value2"}', form: -d "key1=value1&key2=value2"
# -H --header <header/@file>: -H "Content-Type: application/json"

token=`curl -s -X post -d "name_first=eric&name_last=pull&email=123@123.com&password=123456" localhost:5001/auth/register`
token=`echo $token | cut -d\" -f6`
channel_id=`curl -s -X post -d "token=$token&name=channel&is_public=true" localhost:5001/channels/create`
channel_id=`echo $channel_id | cut -d: -f2 | sed 's/}//; s/ //'`
curl localhost:5001/channel/details?token=$token&channel_id=$channel_id
token=`curl -X post -d "email=123@123.com&password=123456" localhost:5001/auth/login`
curl -X post -d "token=$token" localhost:5001/auth/logout 
