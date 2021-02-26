# Crycur

&nbsp;&nbsp;&nbsp;&nbsp;
Crycur is a commandline tool that introduces helpful functionalities for blockchain based crypto currency application.
Including, DSA parameter generation, random transaction block generation, proof of work calculation of transaction blocks
for the chain, and validation for transaction blocks as well as the chain itself.   

&nbsp;&nbsp;&nbsp;&nbsp;
Crycur is OS independent. Meaning that, one can start block or dsa parameter generation and/or mining functions in one
operating system and continue in another. Final result will be valid in all operating systems.

**Implemented by:**

 * [M.Mucahid Benlioglu](https://github.com/mbenlioglu)
 * [Mert Kosan](https://github.com/mertkosan)


## Getting Started

##### Prerequisites:

- [Python](https://www.python.org/) (Python 3 version &ge;3.5; Python 2 version 2.7.x)
- [pip](https://pip.pypa.io/en/stable/) for python package management

##### For GPU Acceleration:

Following are required if you want to use `--gpu` flag

- [CUDA Toolkit](https://developer.nvidia.com/cuda-zone) (Tested on version 10.1)
- [gcc/g++](https://gcc.gnu.org/) (for Linux and Mac) or [Visual Studio](https://visualstudio.microsoft.com/) (for Windows)

### Installation and Running

&nbsp;&nbsp;&nbsp;&nbsp;
Firstly, clone or download this repository, then run the following command in the project root to install needed
dependencies
    
    $ pip install -r requirements.txt

After installation succeeds, you can start using the tool by executing the provided functionalities in the following
format

    $ python crycur.py [COMMAND] [OPTIONS]

For more information execute `$ python crycur.py --help`

####GPU Support

&nbsp;&nbsp;&nbsp;&nbsp;
There is a GPU based implementation included that is available with `--gpu` flag. Make sure you have the requirements
under [GPU Acceleration](#for-gpu-acceleration) section installed to be able to use it. Current implementation uses CUDA
therefore only NVIDIA GPUs are supported.

&nbsp;&nbsp;&nbsp;&nbsp;
Since the problem is compute intensive by nature, utilizing many core GPU architectures greatly improves the performance
as it can be seen in the [performance section](#performance). This performance can still be improved by eliminating
redundant copy operations between device(GPU) and the host(CPU).

&nbsp;&nbsp;&nbsp;&nbsp;
Despite the performance advantages GPU based algorithm is not set to run by default. This is because the current hardware
limitations (NVIDIA GPU) and to keep amount of requirements and installation difficulty minimal to get a working demo.

## Performance

**Testing Environment**

    Hardware:
        CPU:            Intel i9-9980HK
                            Clock: up to 5.0 GHz
                            Cores: 8 cores (w/o hyperthreading)
        GPU:            NVidia GeForce GTX 1650 4GB GDDR5
                            Clock: up to 1.56GHz
                            Cores: 1024 CUDA Cores
                            CUDA compute Capability: 7.5
    Software:
        OS:             Ubuntu 19.10 (Linux 5.3.0-19-generic)
        Python:         3.7.5
        CUDA:           10.1
        NVIDA Driver:   435.21
        C compiler:     gcc 8.3.0
        
    
**Test Results (with default configs)**

    CPU Implementation: 500  PoW/hour
    GPU Implementation: xxxx PoW/hour

## Adapted Cryptocurrency Format

&nbsp;&nbsp;&nbsp;&nbsp;
For the proof of work(PoW) algorithm of [mining](https://en.wikipedia.org/wiki/Bitcoin#Mining), sha3_256 is adapted.
Every link of the chain consists of previous link's PoW, Merkle root hash the transaction block, nonce value and PoW of
link.

&nbsp;&nbsp;&nbsp;&nbsp;
Transaction blocks contains number of transactions which are hashed together to form a link in chain. Lastly, DSA parameters
consist of 2 large primes and a generator number.

**Example Transaction:**

&nbsp;&nbsp;&nbsp;&nbsp;
Each Transaction contains the following sections that makes it a valid transaction.

&nbsp;&nbsp;&nbsp;&nbsp;
**Serial number:** Random number for identifying the transaction

&nbsp;&nbsp;&nbsp;&nbsp;
**p, q & g:** [DSA](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm) parameters. p and q are two large primes and g is a random integer

&nbsp;&nbsp;&nbsp;&nbsp;
**Payer/Payee public keys:** Public keys of sender and receiver of the transaction (used for signature validation)

&nbsp;&nbsp;&nbsp;&nbsp;
**Amount:** Amount of the transaction

&nbsp;&nbsp;&nbsp;&nbsp;
**Signatures r & s:** Signatures of the transaction (for validation) that are signed by receiver(r) and sender(s)


    *** Bitcoin transaction ***
    Serial number: a2ba3e81e8f9acf26bbc2a3ffc9b7565
    p: fb3556601317548f26bafd00cd6fcd38d41b69b8490e0a3412d2de3c76226617bb4922b0520838b1bab60c78c56a276c278a8f759734c7c5fd6d5737d00a06762bc039cab98ce332b0b8c779804b195f8015d8fd9b150247017a1d3e3108403ce19be932d877fe238fbc2159799489a57d41f692ab776368ff18f0dee6fa279d4b906f36d7c2e7ab4557c66715d8395db3306fabc18e6ddd79dc524cffa36e6df0f1b98c6496ffa678ecadd2c57ce276645d4549f321204288b60bd22f14f5828ff1e15e2962f3c9eb7d79f605829c3238d0fe55859f1e64ae3adf2ef0eda1ff164caec8ca461a39c3da114132f7ab03365f2e737797569cb5667dd9a70287eb
    q: 8cb851cb9048afd5a273c6a7bfb6235aab194bcb059ab328d20f99d0c77f360b
    g: c2e3b63406e19b56700ccd170604a146d67a91bf3e6a494687e3947ac72982692ec89988af727aa62ab411be42e0f95701b1fd6c985c34ca4671f700685a7b6d5b3d17c90bd14805aac80083adec92cc90af64ea190e69871248c8c0de997b36ecbe2b2005a927b70691c7e5f58cf0c384e00a41985a6718ddd12ab6d2bbda0254e16f858cf93c9cf983417facb15793eff3e39b5335b0f8c1767b12b9bcbee7c6777d82fa56f286e6a7f0178f4e0cde571d1537871b93be4ef6b5bbb089a7a5bb0c902a655f066573763457ae58b9eba3f25a2ccac712049d21f978dbf1d6b27cb8a20e580fd1a78f3e5b39bb5a7421a0590e86d8d7bad744f2a71c163a1e97
    Payer Public Key (beta): 855c21d06b2f483de1d7549edefe143919bb245dc705435a579bb28c3e674a8e2a072756aaa15fcf5b8f3eaa24ac6516aedb75fe6cadd7c6a896d36b319bc73ddc4f1b0e679acba0a1d7d2cd3c08beed83184ed98a252ea87a0b29d694edd1e3772d5649d48a3ecb60c52d0278a76219b5cac877582683c49d67b64f86a472cad99ea6fb25fe07a872b218a1d93cd2ff33d831689540a590d8ab9faf2807abcc692e06d4268ee7b229be4247a7add2fa7fdfe9ff907719f8b533d2f2bc849eec81188d761af628f2adfae16aa934c47ecef2dd8f50f715110fc223770214432012408aa6c5774580d161dfae7b912ab9258f864529defc2d6f059f83a0f59666
    Payee Public Key (beta): ebf65ae37835fd7b66f200c185ba8684d5afc52b028ee374bbf40c0cc4df313fb6767d1606aea0dfac780fb27e7732ffad654c1c3f6715872f7198f2f98ce86062af9332a37a19dd7110cb792645b0c7c5b6474d8f82bb6c8766b6e970cc4b5ec227c343582e7a0a40cbeda35ccc6e08a187016410ba02e16f454fca21d8c77d241432cb08dcc809c262df65df7420a255b967c51b7435aac730e32bd2804ebe6d7404d4cf83d0b65da0065feed614857281fd23a30c4ef0f0f4dddb220a5fe9d3a88fba96e007413b4706c40a60f52e5db551d835fef1d39d9f27165813439e53d6117d66b1460d304d099c103121374b3095273734d6bb78dd787a8bc2caaf
    Amount: 214 Satoshi
    Signature (r): 6ce1cdf266bbf3fd858f5fe7b014219d7f5cf9c2c8787fb5d48ab3a953088d37
    Signature (s): 164c87ae0e6f80e158da24c37d9f462900056559d13bc657b38c7c9b24592aa0

**Example Link in Chain:**
    
&nbsp;&nbsp;&nbsp;&nbsp;
A link in the chain contains 4 lines of information for proof of work (PoW). First line is the previous transaction's PoW,
second line is the [Merkle root](https://en.wikipedia.org/wiki/Merkle_tree) hash of the transaction. Third line is a random
128-bit integer (by default, can be changed) to satisfy PoW difficulty (e.g. starting with six 0's), and finally the hash
of these 3 lines as PoW of the current chain.
    
    00000053e1ff1ef3cb49b937fac8b519b4639cf367a6a1b6a71d2455e833856f
    b88721f1a78f92b63b95f8242f66e361f26f17f770bb8ee543cf319a023a001c
    dd00f3ca711707a40e7632939664e147
    0000001c8031da7eb0ea1eb3f01e236c1da7600eadcdf03e9184a2b741877fc2

## Acknowledgement
_This project initially created as a part of the term project for **CS411 - Cryptography** lecture of **Sabanci University**_
