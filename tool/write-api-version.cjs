const fs = require('node:fs');
const path = require('node:path');
const YAML = require('yaml');

const version = process.argv[2];

if (!version) {
  throw new Error('Missing API version');
}

const files = [
  '../openapi/openapi.yaml',
];

for (const file of files) {
  const filePath = path.resolve(__dirname, file);

  if (!fs.existsSync(filePath)) {
    console.warn(`Skipping missing file: ${filePath}`);
    continue;
  }

  const document = YAML.parseDocument(
    fs.readFileSync(filePath, 'utf8')
  );

  if (document.errors.length > 0) {
    throw new Error(
      `Invalid YAML in ${filePath}:\n${document.errors.join('\n')}`
    );
  }

  if (!document.get('info')) {
    document.set('info', {});
  }

  document.setIn(['info', 'version'], version);

  fs.writeFileSync(filePath, document.toString());

  console.log(`Updated ${filePath} to version ${version}`);
}
