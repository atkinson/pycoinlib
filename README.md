<div id="top"></div>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />

<h3 align="center">pycoinlib</h3>

  <p align="center">
    Python client for the coinlib.io API endpoints.
    <br />
    <a href="https://github.com/atkinson/pycoinlib"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/atkinson/pycoinlib/issues">Report Bug</a>
    ·
    <a href="https://github.com/atkinson/pycoinlib/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple API wrapper for the coinlib.io API.

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- GETTING STARTED -->

### Installation

1. Get a free API Key at [https://coinlib.io/](https://coinlib.io/)
2. Install the package
   ```sh
   pip install pycoinlib
   ```
3. Add your API in as an env var
   ```sh
   export COINLIB_API_KEY="YOUR API KEY";
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```py
from pycoinlib import coinlib, GLOBAL, COIN, COINLIST, RANK_ASC

print(coinlib(GLOBAL))

print(coinlib(COINLIST, order=RANK_ASC))

print(coinlib(COIN, symbol="ETH"))
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Rich Atkinson - [@tkinson](https://twitter.com/tkinson)
Project Link: [https://github.com/atkinson/pycoinlib](https://github.com/atkinson/coinlib)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [requests](https://docs.python-requests.org/en/latest/)
* [coinlib.io](https://coinlib.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/atkinson/pycoinlib.svg?style=for-the-badge
[contributors-url]: https://github.com/atkinson/pycoinlib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/atkinson/pycoinlib.svg?style=for-the-badge
[forks-url]: https://github.com/atkinson/pycoinlib/network/members
[stars-shield]: https://img.shields.io/github/stars/atkinson/pycoinlib.svg?style=for-the-badge
[stars-url]: https://github.com/atkinson/pycoinlib/stargazers
[issues-shield]: https://img.shields.io/github/issues/atkinson/pycoinlib.svg?style=for-the-badge
[issues-url]: https://github.com/atkinson/pycoinlib/issues
[license-shield]: https://img.shields.io/github/license/atkinson/pycoinlib.svg?style=for-the-badge
[license-url]: https://github.com/atkinson/pycoinlib/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
