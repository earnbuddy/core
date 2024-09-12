THIS PROJECT IS NOT FINISHED YET AND IS STILL IN DEVELOPMENT
PLEASE USE THIS PROJECT AT YOUR OWN RISK

# Features
- Easy to use
- Works without port forwarding
- Auto updating clients
- Easy to add new earners
- Easy to add new devices

# Parts

## client
Python client see [github.com/earnbuddy/client](https://github.com/earnbuddy/client)

## app
Svelte app

## server
FastAPI server with a database also serves the svelte app

## Earners
| Name                                                                                                    | Residential/Home ISP | 	Datacenter/Hosting/VPS | 	Limit per Account | Devices per IP | Payment                  | ARM                   | x86                | Docker               | Current support             | Note                                                          |
|---------------------------------------------------------------------------------------------------------|----------------------|-------------------------|--------------------|----------------|--------------------------|-----------------------|--------------------|----------------------|-----------------------------|---------------------------------------------------------------|
| [EarnApp](https://earnapp.com/i/1BGXdR4W)                                                               | :white_check_mark:   | :x:                     | No limit           | 1              | Paypal, Gift Card        | :white_check_mark:    | :white_check_mark: | :x:                  | :x: because no docker       |                                                               |
| [PacketStream](https://packetstream.io/?psr=6RSL)                                                       | :white_check_mark:   | :x:                     | No limit           | 1              | Paypal                   | :white_check_mark:    | :white_check_mark: | :white_check_mark: ️ | :white_check_mark:          |                                                               |
| [Honeygain](https://r.honeygain.me/MZOND7F3D1)                                                          | :white_check_mark:   | :x:                     | 10                 | 1              | Crypto, Paypal           | :x:                   | :white_check_mark: | :white_check_mark: ️ | :white_check_mark:          | Needs some work with the device name when container recreated |
| [Pawns](https://pawns.app/?r=4874817)                                                                   | :white_check_mark:   | :x:                     | No limit           | 1              | Crypto, Paypal           | ️️ :white_check_mark: | :white_check_mark: | :white_check_mark: ️ | :white_check_mark:          |                                                               |
| [Speedshare](https://speedshare.app/?ref=matthijz98)                                                    | :white_check_mark:   | :x:                     | No limit           | 1              | Gift Card                | :white_check_mark:    | :white_check_mark: | :white_check_mark: ️ | :white_check_mark:          | using https://github.com/MRColorR/speedshare                  |
| [PacketShare](https://www.packetshare.io/?code=8366031CC65F0B18)                                        | :white_check_mark:   | :x:                     | No limit           | 1              | Paypal                   | :x:                   | :white_check_mark: | :x: ️                | :x:  because no docker      |                                                               |
| CryptoProxy                                                                                             | :white_check_mark:   | :x:                     | No limit           | 1              | Crypto                   | :x:                   | :x:                | :x:                  | :x:  android phone only     |                                                               |
| [Grass](https://app.getgrass.io/register/?referralCode=RVNn4g7UKju8PC5)                                 | :white_check_mark:   | :x:                     | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          | using https://github.com/MRColorR/get-grass                   |
| [EarnFM](https://earn.fm/ref/MATT8D0N)                                                                  | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto, Paypal, Giftcard | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          |                                                               |
| Peer2Profit                                                                                             | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | ?                     | ?                  | ?                    | ?                           | Can not signup at the moment                                  |
| [ProxyRack](https://peer.proxyrack.com/ref/m5muudlu4rae0rwh11rlwrtsdnm2jvudkgajebh4)                    | :white_check_mark:   | :white_check_mark:      | 500                | 1              | Paypal                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          |                                                               |
| [Repocket](https://link.repocket.com/E8Zq)                                                              | :white_check_mark:   | :white_check_mark:      | No limit           | 2              | Paypal, Wise             | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          |                                                               |
| [Traffmonetizer](https://traffmonetizer.com/?aff=1716418)                                               | :white_check_mark:   | :white_check_mark:      | No limit           | No limit       | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          |                                                               |
| [Proxylite](https://proxylite.ru/?r=GOHSB9A5)                                                           | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | docker hub page not working |                                                               |
| [Bitping](https://bitping.com)                                                                          |                      |                         |                    |                |                          |                       |                    |                      |                             |                                                               |
| [Mysterium](https://mystnodes.co/?referral_code=UHrYl5EeDPe2PWoYCDXcVkFsncvj7art1sWp91OE)               | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          | Need setup trough webui needed                                |
| [ByteLixir](https://bytelixir.com/r/U4B3KLSPLWUO)                                                       | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :x:                  | :x:                         | No Docker                                                     |
| [GaGaNode](https://www.gaganode.com/)                                                                   | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          | using: https://github.com/XternA/gaga-node                    |
| [BearShare](https://app.bearshare.app/register?ref=933888aacaa3f989fc069ba7bf9afc1fa53d31e8cb4210e246f) | :white_check_mark:   | :white_check_mark:      | No limit           | 1              | Crypto                   | :white_check_mark:    | :white_check_mark: | :white_check_mark:   | :white_check_mark:          |                                                               |


## Install manual
### server
Docker and docker-compose is required



### client
##
docker

1. create a .env file see the .env.example or set them on the docker container
2. start the client script
