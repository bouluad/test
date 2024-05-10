        VERSION=$(xmllint --xpath "//*[local-name()='project']/*[local-name()='version']/text()" pom.xml)
        echo "::set-output name=version::$VERSION"

        VERSION=$(xmllint --xpath "//*[local-name()='project']/*[local-name()='version']/text()" pom.xml)
        if [ -z "$VERSION" ]; then
          VERSION="1.0.0"
        fi
        echo "::set-output name=version::$VERSION"
