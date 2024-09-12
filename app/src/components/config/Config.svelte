<script>
	import EarnerConfig from './EarnerConfig.svelte';
	import ProxyrackUUIDList from './ProxyrackUUIDList.svelte';

</script>

<div>
	<h1 class="mt-2 text-2xl text-white font-medium">Settings</h1>
	<div class="flex flex-col gap-4">
		<EarnerConfig
			name="HoneyGain"
			img="/earners/Honeygain.png"
			description=""
			signup_link="https://r.honeygain.me/MZOND7F3D1"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<EarnerConfig
			name="EarnFM"
			img="/earners/EarnFM.webp"
			description=""
			signup_link="https://earn.fm/ref/MATT8D0N"
			options={[{name: 'api_key'}]}
		/>

		<EarnerConfig
			name="PacketStream"
			img="/earners/PacketStream.png"
			description=""
			signup_link="https://packetstream.io/?psr=6RSL"
			options={[{name: 'cid'}]}
		/>

		<EarnerConfig
			name="Pawns"
			img="/earners/Pawns.png"
			description=""
			signup_link="https://pawns.app/?r=4874817"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<EarnerConfig
			name="Grass"
			img="earners/Grass.png"
			description=""
			signup_link="https://app.getgrass.io/register/?referralCode=RVNn4g7UKju8PC5"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<ProxyrackUUIDList
			name="Proxyrack"
			img="earners/Proxyrack.png"
			description=""
			signup_link="https://peer.proxyrack.com/ref/m5muudlu4rae0rwh11rlwrtsdnm2jvudkgajebh4"
		/>

		<EarnerConfig
			name="Repocket"
			img="/earners/Repocket.png"
			description=""
			signup_link="https://link.repocket.com/E8Zq"
			options={[{name: 'email'}, {name: 'api_key'}]}
		/>

		<EarnerConfig
			name="SpeedShare"
			img="/earners/SpeedShare.png"
			description=""
			signup_link="https://speedshare.app/?ref=matthijz98"
			options={[{name: 'AuthCode'}]}
		/>

		<EarnerConfig
			name="Traffmonetizer"
			img="/earners/traffmonetizer.png"
			description=""
			signup_link="https://traffmonetizer.com/?aff=1716418"
			options={[{name: 'token'}]}
		/>

		<EarnerConfig
			name="PacketShare"
			img="/earners/PacketShare.svg"
			description=""
			signup_link="https://www.packetshare.io/?code=8366031CC65F0B18"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<EarnerConfig
			name="GaGaNode"
			img="/earners/gaga-logo.svg"
			description=""
			signup_link="https://www.gaganode.com/"
			options={[{name: 'token'}]}
		/>

		<EarnerConfig
			name="BearShare"
			img="/earners/bear-share.png"
			description=""
			signup_link="https://app.bearshare.app/register?ref=933888aacaa3f989fc069ba7bf9afc1fa53d31e8cb4210e246f"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<EarnerConfig
			name="SpideNetwork"
			img="/earners/spide-network.png"
			description=""
			signup_link="https://spide.network/register.html?543ec4"
			options={[{name: 'email'}, {name: 'password'}]}
		/>

		<EarnerConfig
			name="NodePay"
			img="/earners/NodePay.svg"
			description="See <a href='https://github.com/XternA/income-generator/wiki/NodePay'>https://github.com/XternA/income-generator/wiki/NodePay</a> for more info"
			signup_link="https://app.nodepay.ai/register?ref=ci6TGnbNA9UEKMX"
			options={[{name: 'cookie'}]}
		/>
	</div>
</div>
