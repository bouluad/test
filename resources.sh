for ns in $(kubectl get namespaces -o jsonpath="{.items[?(@.metadata.name | startsWith('cdpjen'))].metadata.name}"); do
  echo "Namespace: $ns"
  kubectl get deployment jenkins-master -n $ns -o jsonpath="{.spec.template.spec.containers[*].resources}"
  echo
done
