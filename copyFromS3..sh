#!/bin/bash
#$1 <AWS_ACCESS_KEY_ID>
#$2 <AWS_SECRET_ACCESS_KEY>
#$3 <endpoint-url>
#$4 <copyFromPath>
#$5 <destinationPath>
#$6 <fileName>
set -ex
awsAccessKeyId=$1
awsSecretAccessKey=$2
endpointurl=$3
srcPath=$4
destPath=$5
fileName=$6
pyArgs=""

export AWS_ACCESS_KEY_ID=$awsAccessKeyId
export AWS_SECRET_ACCESS_KEY=$awsSecretAccessKey


echo $awsAccessKeyId
echo $awsSecretAccessKey
echo $endpointurl
echo $srcPath
echo $destPath
echo $fileName
echo $propFile
STR=$fileName
echo "verification log no 1"
sub='#'

if [[ "$fileName" == *"$sub"* ]]; then
fname=$(echo $STR | cut -f1 -d#)
pyArgs=$(echo $STR | cut -f2 -d#)
fileName=$fname

fi

echo $fileName
echo $pyArgs
aws --endpoint-url $endpointurl s3 cp $srcPath$fileName $destPath$fileName
echo "running the python script"
python3 $destPath$fileName $pyArgs