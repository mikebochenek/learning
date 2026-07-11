# Intro & high level

been thinking that: _we are integrators, not developers_

notes and concepts that should help long term
* k8s: pods vs. nodes (again)
* helm: youtube or pluralsight
* ansible: more non-trivial examples
* Azure play around
* inner workings of git

# Links

* generally: google, stackoverflow, youtube, pluralsight
* [1️⃣ DevOps Interview Questions 👉 https://lnkd.in/dDcMy8Hi](https://github.com/bregman-arie/devops-exercises)
* [2️⃣ System Design Interview Repo 👉 https://lnkd.in/dJrNE4j4](https://github.com/karanpratapsingh/system-design)
* [3️⃣ Linux Interview Guide 👉 https://lnkd.in/dY5vdmXt](https://github.com/trimstray/test-your-sysadmin-skills)
* [4️⃣ Kubernetes Interview Questions 👉 https://lnkd.in/d2Q_tyyZ](https://github.com/hclpandv/devops-training-material/blob/main/kubernetes/k8s-interview-questions.md)
* [5️⃣ AWS Interview Questions 👉 https://lnkd.in/dK-Wv5M8](https://github.com/Devinterview-io/aws-interview-questions)
* [6️⃣ Terraform Interview Repo 👉 https://lnkd.in/deMYZcHf](https://github.com/rkm-ravi94/awesome-devops-interview/blob/main/terraform.md)
* [7️⃣ Behavioral Interview Frameworks 👉 https://lnkd.in/d2CUiMqK](https://github.com/ashishps1/awesome-behavioral-interviews)

# Apigee

A good place to start: **https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee** — the "What is Apigee?" overview — and then follow it straight into the **"Build your first API proxy"** tutorial (linked from that same page). That combo gives you the concept plus a hands-on proxy in under an hour. Skip anything you find under `docs.apigee.com` — that's the older "Apigee Edge" doc set; you want the current Apigee X / Google Cloud docs instead.

As for describing it to an experienced developer — the fastest framing:

**Apigee is a reverse proxy for your APIs, with policy-driven middleware instead of code.**

More concretely:

- You put Apigee in front of a backend service (REST, gRPC, SOAP, GraphQL — it doesn't care). Clients call the Apigee-fronted URL instead of hitting your backend directly.
- Between the client and your backend, you attach **policies** — XML/JSON config blocks, not code — for things like OAuth/API key verification, rate limiting/quotas, request/response transformation (XML↔JSON), caching, spike arrest, logging, and routing logic.
- Because clients never talk to your backend directly, you can change, version, or migrate your backend without breaking consumers — it's the same value prop as an API gateway/facade pattern, just with a GUI + config layer instead of writing that middleware yourself.
- It also bundles the "business" side of API management: a developer portal for external consumers, API key/app registration, analytics on traffic, and monetization (metering/billing for API usage) if you're exposing APIs commercially.

If your developer friend has used **Kong, AWS API Gateway, or Envoy**, the honest comparison is: same core idea (gateway + policies), but Apigee leans more heavily into the full API-lifecycle/business side (developer portal, monetization, analytics) rather than being just a lightweight gateway — which makes it heavier-weight but more of a full "API product management" platform than a pure infrastructure gateway.

## Tracing

**https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/view-with-trace**