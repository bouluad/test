        VERSION=$(xmllint --xpath "//*[local-name()='project']/*[local-name()='version']/text()" pom.xml)
        echo "::set-output name=version::$VERSION"
