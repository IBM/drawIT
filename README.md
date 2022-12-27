# drawIT
Create IT architecture diagrams from code or tooling.

## Overview

drawIT creates diagrams that can be viewed in IBM2 on diagrams.net.

Use cases:
- Code-to-Diagram: 
  - Refer to examples folder.
  - Input is python code.
  - Output is diagrams.net xml file.
- RIAS-to-Diagram:
  - Refer to rungui.sh or runrias.sh in scripts folder.
  - Input is from RIAS APIs.
  - Output is diagrams.net xml file.
- JSON-to-Diagram:
  - Refer to rungui.sh or run.sh in scripts folder.
  - Input is tool-generated JSON/YAML.
  - Output is diagrams.net xml file.

Notes:
  - Diagrams can be exported to jpg, pdf, png, or svg from diagrams.net.
  - Future: Export diagram to jpg, pdf, png, or svg directly from drawIT using diagrams.net CLI.

## Running drawIT

- Prereqs:
  - Python 3.10.5
  - pandas 1.4.2
  - PyYAML 6.0
  - requests 2.28.0
  - urllib3 1.26.9
- Scripts folder contains scripts for input of JSON, YAML, or RIAS.
- Examples folder contain input examples.
- Scripts folder contains scripts for input of JSON, YAML, or RIAS.

<!--
2. Using NodeJS: 
- npm start 
- curl -X POST --data-binary @test/drawit.json.zip -H "Content-Type: application/zip" http://localhost:8080/drawit/<identifier\>
- curl returns drawio xml directly (plus errors/warnings).
3. Using Podman (or Docker):
- podman build . -t drawit
- podman run -p 41920:8080 -d drawit
- curl -X POST --data-binary @test/drawit.json.zip -H "Content-Type: application/zip" http://localhost:41920/drawit/<identifier\>
- curl returns drawio xml directly (plus errors/warnings).
-->

<!--
![drawIT Flow](/images/drawitFlow.png "DrawIT Flow")

## RIAS Steps

1. Create API Key if not already created:
- Login to [IBM Cloud Portal](https://cloud.ibm.com/).
- Go to **Manage** and select **Access (IAM)**.
- Go to **API keys** and select **Create an IBM Cloud API key**.
- Copy the API Key.
2. Convert RIAS to drawio file(s):
- Start **Draw IT** application.
- Copy API Key into **API Key** field.
- (Optional) Copy Account ID into **Account ID** field.
- Leave **YAML File** blank.
- Use default directory or click **Select Directory** to change directory.
- Select **Region**.
- Select **Detail Level**.
- Select **Diagram Type**.
- Select **File Organization**.
- Select **Generate**.
3. View in diagrams.net:
- Install and start [diagrams.net application]
(https://github.com/IBM/it-architecture-diagrams/releases).
- Click **Open Existing Diagram** and select a diagrams.net file.
-->

## Features Supported

- Cloud
- Region
- Availability Zone
  - Public Gateway
  - VPN Gateway
- VPC
  - Implicit Router
  - Private & Public ALB
  - Private & Public NLB
- Subnet
  - Instances
  - Floating IP
- Public Network
  - Internet
  - User
- Enterprise Network
  - User 

## References

- [buildIT](https://github.com/IBM/buildit)
- [IT Architecture Diagrams](https://github.com/IBM/it-architecture-diagrams)
- [Code Pattern](https://github.com/IBM/codepattern-multitier-vpc)

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

