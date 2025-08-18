# Python container with NeuroPilot

This is a ready-to-go container with pre-configured settings and extensions for NeuroPilot.
Updates to NeuroPilot are also *sometimes* tested against this container.

## Get started

You can either:

- Use this repo as a template; or
- Pull down a pre-built image uploaded to the GitHub Container Registry.

### Use this repository as a template

1. Click the "Use this template" button at the top-right of the repo area. Follow the steps to create a repo with this template.
2. Open this in a container environment, such as Docker or GitHub Codespaces.
3. Dependencies should be automatically installed (using `pip`) and pre-configured, ready-to-go. If not, tell Docker to run the Dockerfile. <!-- todo: instructions -->
4. Choose to install the recommended extensions.
5. Remove the following files, as they are not needed:

- .github/workflows/*
- .github/README.md
- .dockerignore

### Pull down a pre-built image

An image with dependencies pre-installed is available at `ghcr.io/VSC-NeuroPilot/python-pip-image` with the latest version of this repo.

- A specific version of the image can be accessed by appending `@sha256:<SHA-256 of the image>` to the image URL.
- If you want to use the image released for a specific version of NeuroPilot, append `:<version tag>` to the image URL instead.

> [!Note]
> Be aware that not all NeuroPilot versions have an associated container version. Versions published prior to 2.1.0 do not have associated container versions, and small changes do not often come with an associated container version.

### Other container images

Refer to the `Container templates` topics on the NeuroPilot Docs for pre-configured container images with other languages.
