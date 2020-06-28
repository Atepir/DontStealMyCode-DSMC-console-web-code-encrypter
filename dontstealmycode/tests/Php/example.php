<?php
	$postdata = http_build_query(
		array(
				'apikey' => 'YOUR-API-KEY',
				'speaker' => 'Joanna',
				'text' => 'the quick brown fox jumps over the lazy dog',
			)
		);
	$opts = array('http' =>
		array(
			'method'  => 'POST',
			'header'  => 'Content-type: application/x-www-form-urlencoded',
			'content' => $postdata
		)
	);
	$context  = stream_context_create($opts);
	$result = file_get_contents('https://api.ttsmp3.com/v1/', false, $context);
	$resultarray = json_decode($result, true);
	echo "<pre>".print_r($resultarray, true)."</pre>";

?>
<audio controls>
	<source src="<?php echo $resultarray['data']['URL']; ?>" type="audio/ogg">
</audio>
