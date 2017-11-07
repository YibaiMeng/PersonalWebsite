# Setting up OpenVPN

For obvious reasons, I need a VPN. After experimenting with PPTP, L2TP/IPSec, IPSec, I've decided to give [OpenVPN](https://openvpn.net) a try. So I signed up for ProtonVPN, a free (as in freedom) VPN service by the Swiss based organization ProtonMail. The experience is great, the stability even greater! So I decided to throw away my old IPSec configuration and switch to OpenVPN instead.

## Installing Server-Side Software

The Server side software is not diffcult to install. You could use your server's package manager to download a pre-built version, or complie it yourself. For example, in Ubuntu/Debian, use

```shell
sudo apt-get install openvpn
```

Or compile it like I did

```shell
wget https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.gz
# use the up to date tar archive on https://openvpn.net
tar xfz openvpn-2.4.4.tar.gz
cd openvpn-2.4.4
./configure
make
make install # might need to put sudo before that
```

Note when configuring, a few error messages may appear. For the error `configure: error: ssl is required but missing`, you will need to install `libssl-dev`.
```shell
sudo apt-get install libssl-dev
```
For the error `configure: error: lzo enabled but missing`
```shell
sudo apt-get install liblzo2-dev
```
For the error `configure: error: libpam required but missing `
```shell
sudo apt-get install libpam0g-dev
```
Great thanks for [deadcode](https://stackoverflow.com/users/2640725/deadcode)'s [advice](https://stackoverflow.com/a/28431851) on Stack Overflow.

Next, set up PKI and CA! TODO