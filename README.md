# synapse-test-plugin
A sample plugin for testing that the Synapse internal API is actually being called

# Install

`pip install https://github.com/turt2live/synapse-test-plugin/tarball/master`

# Usage

Add this to your synapse homeserver.yaml:

```yaml
internal_api_plugins:
- module: synapse_test_plugin.test.TestPlugin
  config: {}
```
